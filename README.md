# Japan Disaster Information Assistant Slack Bot

## Overview
This Python script operates a Slack bot designed to provide real-time updates on disasters in Japan, such as earthquakes, tsunamis, and other emergencies. It sources its information from NERV's Mastodon instance and posts updates directly to a Slack channel.

## Requirements
- Python 3.x
- Pipenv for managing dependencies
- Requests, BeautifulSoup, Huey: These dependencies will be installed via Pipenv

## Setup Instructions
1. **Environment Configuration**: Set the `SLACK_WEBHOOK_URL` in your environment variables. This should be the URL of your Slack channel's Incoming Webhook.
2. **Database Initialization**: On the first run, the script will automatically create a SQLite database (`posts.db`) to store posts.
3. **Pipenv Setup**: Run `pipenv install` to set up your virtual environment and install the required packages.

## Key Features
- **Disaster Information Updates**: Retrieves updates from NERV's Mastodon account (https://unnerv.jp/api/v1/accounts/12/statuses).
- **Slack Integration**: Uses Slack's Incoming Webhooks API for posting updates.
- **Database Functionality**: Stores records of posts in a SQLite database to prevent reposting.
- **Scheduled Updates**: Configured to check for new posts every minute using Huey, with retry and delay options.

## How to Use
Execute the script within the Pipenv environment:

```bash
pipenv run huey_consumer.py app.huey
```

## Future Enhancements
- **API Endpoint Customization**: Users can modify the Mastodon API URL in the script to target different accounts or instances.
- **Translation Module**: Integration of a feature for translating posts from Japanese to English would greatly enhance the bot's utility.
- **Environment Variables Check**: Ensure the `SLACK_WEBHOOK_URL` is accurately set for effective Slack integration.

## Contributing
Contributions to expand the bot's functionality, like adding a translation feature or optimizing performance, are welcome. Follow best coding practices and include thorough documentation for your changes.

## Project Objective
This bot is dedicated to facilitating swift communication of disaster-related information in Slack, contributing to prompt and informed responses to emergencies in Japan.
