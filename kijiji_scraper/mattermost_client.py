import mattermost


class MattermostClient:
    def __init__(self, mattermost_config):
        self._host = mattermost_config.get("mm_host")
        self._port = mattermost_config.get("mm_port")

        self._mattermost = mattermost.MMApi("http://{}:{}/api".format(self._host, self._port))
        self._mattermost.login(
            bearer=mattermost_config.get("mm_access_token")
        )

        self._team = self.get_team_by_name(mattermost_config.get("mm_team"))
        self._channel = self._mattermost.get_channel_by_name(
            team_id=self._team.get("id"),
            channel_name=mattermost_config.get("mm_channel")
        )

    def get_team_by_name(self, name):
        for team in self._mattermost.get_teams():
            if team.get("display_name") == name:
                return team
        raise ValueError("{} team doesn't exist.".format(name))

    def post_ads(self, ads):
        """"""
        for ad_info in ads.values():
            message = "{price}\n{title}\n{details} \n{url}".format(
                title=ad_info.get("Title"),
                price=ad_info.get("Price"),
                details=ad_info.get("Details"),
                url=ad_info.get("Url")
            )
            self._mattermost.create_post(
                self._channel.get("id"),
                message=message
            )
