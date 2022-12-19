## Gridly
Gridly creates grids from Last.fm listening history. It creates different sized collages for your top albums, artists or songs.

![alt text](./examples/Album.jpeg)

#### How to install
Make sure to have Python installed. In addition to that, following three libraries must be installed:

- Pillow
- requests
- spotipy

While in the root folder, they can be installed using the following command:

    pip install -r requirements.txt

In first run Last.fm API key (https://www.last.fm/api/account/create), Spotify client ID and secret (https://developer.spotify.com/dashboard) will be asked.
 
After this configuration you are good to go!

#### How to use
Gridly takes three positional arguments.

    x             Horizontal size of the collage
    y             Vertical size of the collage
    username      Last.fm username

Here is an example run. Without extra arguments Gridly creates a collage for users top albums from the last year.

    python gridly.py 5 5 example_user

With optional arguments it is possible to create collages for artists and songs. It is also possible to skip items that are missing artwork.

    -h, --help    show this help message and exit
    --album, -a   Create album collage
    --artist, -b  Create artist collage
    --song, -s    Create song collage
    --name, -n    Print names
    --skip        Skip items without covers
    --exclude EXCLUDE [EXCLUDE ...], -e EXCLUDE [EXCLUDE ...] 
                  Exclude artists
    --config, -c  Configure the config file

