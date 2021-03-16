from argparse import ArgumentParser

from pyxiv import PyxivBrowser, PyxivConfig, PyxivDownloader

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config", type=str, default="config.json", help="a json file which stores pyxiv configs")
    args = parser.parse_args()

    config = PyxivConfig().load(args.config)
    downloader = PyxivDownloader(config)

    downloader.download_all()
    # downloader.download_illusts()
    # downloader.download_users()
