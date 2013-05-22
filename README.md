Genesis is a toolkit for building worlds programatically. The central functional unit of Genesis is the Map; a map is an arbitrarily sized piece of terrain, which may or may not contain bodies of water, mountain ranges complete with volcanos and caverns, forests, and other natural features. If desired, unnatural structures can be placed, such as cities, dungeons, and other artifical or otherworldly features.

#Installation
````
virtualenv2 genesis_env/
cd genesis_env/
git clone git://github.com/therealfakemoot/Genesis.git genesis/
````

#Usage:
At the moment, there is only a demo of the topological map created by phase one of the world generation process. To use the demo:

````
cd genesis_env/
source bin/activate
python genesis/core/demo.py
````

*_WARNING_*
Trying to contour plot a map larger than 1000x1000 may *completely* bomb your memory. Be careful. Start gradually.

#Notes
This is extemely alpha software. Only phase one, heightmap generation, is fully operational. Watch dev for changes, I'm only going to merge dev into master as phases are completed.

#Progress
- [x] Phase One: Height Map Generation and Display
- [ ] Phase Two: Water Placement
- [ ] Phase Three: Biome Placement
- [ ] Phase Four: Artificial Feature Generation
- [ ] Phase Five: Artifical Feature Placement
