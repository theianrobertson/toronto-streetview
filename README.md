# All Toronto Addresses

Mucking about with a Twitter bot to tweet out pictures of every address in Toronto. Check out and follow [@EveryTOAddress](https://twitter.com/EveryTOAddress) to see it in action!

## How do I do it?

- Install `requirements.txt`
- Run `data_pull.py` - that downloads the list of things and creates `big_list.txt`
- Create a file `config.py` which assigns:
    + `API_KEY` to your [Google API key](https://developers.google.com/maps/documentation/streetview/get-api-key)
    + `APP_KEY` to your Twitter app key
    + `APP_SECRET` to your Twitter app secret
    + `OAUTH_TOKEN` to your Twitter oauth token
    + `OAUTH_TOKEN_SECRET` to your Twitter oauth token secret.
- Run `main.py`, which grabs a random address from `big_list.txt`, saves as `to_upload.jpeg`, and uploads.
- ???
- Profit