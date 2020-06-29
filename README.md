# YouTube-DL-Watch-Later-Playlist <!-- omit in toc -->

> Python script to download YouTube videos from your Watch Later Playlist

[![Open Issues](https://badgen.net/github/open-issues/longpdo/youtube-dl-watch-later-playlist)](https://github.com/longpdo/youtube-dl-watch-later-playlist/issues)
[![License](https://badgen.net/github/license/longpdo/youtube-dl-watch-later-playlist)](LICENSE)

[Report Bug](https://github.com/longpdo/youtube-dl-watch-later-playlist/issues) · [Request Feature](https://github.com/longpdo/youtube-dl-watch-later-playlist/issues)

<!-- TABLE OF CONTENTS -->
## Table of Contents <!-- omit in toc -->

* [About The Project](#about-the-project)
  * [Built With](#built-with)
  * [Features](#features)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Customize](#customize)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Screenshot][product-screenshot]](https://github.com/longpdo/youtube-dl-watch-later-playlist/)

`youtube-dl-watch-later-playlist.py` is a python script to automatically download all YouTube videos from your current Watch Later Playlist. The script will start `Chromedriver` and login to your Google Account.

Logging in to your Google Account is currently done by signing up at `stackoverflow.com` via Google, since logging in to Google directly at YouTube won't work due to Google not trusting automated Webbrowsers like `Chromedriver`. The workaround works, since `stackoverflow.com` is one of the trusted apps by Google.

The script also works when your Google Account has `Two-Factor Authentication` activated and will wait for 5 minutes before throwing a TimeoutException.

After successfully logging in to Google and being redirected to `stackoverflow.com`, `Chromedriver` will move to `https://www.youtube.com/playlist?list=WL` and crawl the links for all the videos in the playlist and the script will start downloading them with `youtube-dl`.

### Built With

* [Python 3.7.6](https://www.python.org/downloads/)
* [Selenium](https://pypi.org/project/selenium/)

### Features

* Colored Terminal output with [termcolor](https://pypi.org/project/termcolor/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3

```sh
# Install via brew on macOS
brew install python
```

For Linux and Windows refer to [this](https://realpython.com/installing-python/).

* Chromedriver

```sh
brew cask install chromedriver
```

For Linux and Windows refer to [this](https://sites.google.com/a/chromium.org/chromedriver/downloads).

* youtube-dl

```sh
brew install youtube-dl
```

For Linux and Windows refer to [this](http://ytdl-org.github.io/youtube-dl/download.html).

### Installation

1: Fork the repository (using the `Fork` button at the top)

2: Clone the repository

```sh
# Replace {YOUR_USERNAME} with your actual username
git clone https://github.com/{YOUR_USERNAME}/youtube-dl-watch-later-playlist.git
```

3: Change directory to youtube-dl-watch-later-playlist

```sh
cd youtube-dl-watch-later-playlist
```

4: Install python requirements

```sh
pip3 install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

* Start the download script

```sh
python3 youtube-dl-watch-later-playlist.py
```

* The script will prompt you for your `google username` and your `google password`

![Usage Input Screenshot][usage-input-screenshot]

* After your input, the script will start an automated Chrome browser with Selenium and sign up to `stackoverflow.com` with your Google credentials.
* If you entered wrong credentials you will be prompted for them again in your Terminal.

![Usage Wrong Input Screenshot][usage-wrong-input-screenshot]

### Customize

* You can change the download folder for the videos in line 11:

```text
download_folder = '~/Downloads/'
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Workaround for Google Login issue](https://gist.github.com/ikegami-yukino/51b247080976cb41fe93#gistcomment-3181443) - 'This browser or app may not be secure'
* [youtube-dl](http://ytdl-org.github.io/youtube-dl/)

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/example.gif
[usage-input-screenshot]: images/example_input.gif
[usage-wrong-input-screenshot]: images/example_wrong_input.gif
