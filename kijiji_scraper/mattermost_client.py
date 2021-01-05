import mattermost
import yaml


class MattermostClient():
    def __init__(self, mattermost_config):
        self._host = mattermost_config.get("mm_host")
        self._port = mattermost_config.get("mm_port")

        self._mattermost = mattermost.MMApi("http://{}:{}/api".format(self._host, self._port))
        self._mattermost.login(bearer=mattermost_config.get("mm_access_token"))
        print([i for i in self._mattermost.get_teams()])
        # team = self._mattermost.get_team("NAS")
        # self._channel = self._mattermost.get_channel_by_name(
        #     team_id=team.get("id"),
        #     channel_name=mattermost_config.get("mm_channel")
        # )

    def post_ads(self, ads):
        """"""
        pass
        # self._mattermost.create_post(self._channel.get("id"))


if __name__ == '__main__':
    mm = MattermostClient(
        {
            "mm_host": "192.168.68.107",
            "mm_port": "5180",
            "mm_access_token": "iiq31oaj7jbn8m4zoonznopy9w",
            "mm_channel": "Kijiji"
        }
    )
