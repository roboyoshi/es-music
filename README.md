# es-music
Create an index of your music collection with python and elasticsearch

## Use

```sh
# Install dependencies:
pip3 install mutagen


# Start ELasticSearch:
docker run --rm --name es-music -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.6.0

# Run the Parser:
python3 parser.py --library=~/Music
```