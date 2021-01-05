import mattermost
import yaml


class MattermostClient():
    def __init__(self):
        mm = mattermost.MMApi("https://mattermost.example.com/api")
        mm.login("user@example.com", "my-pw")
        # alternatively use a personal-access-token/bot-token.
        # mm.login(bearer="my-personal-access-token")


if __name__ == '__main__':
    filename = "../config.yaml"
    with open(filename, "r") as config_file:
        email_config, mm_config, urls_to_scrape = yaml.safe_load_all(config_file)
    print(email_config)
    print(mm_config)
    print(urls_to_scrape)