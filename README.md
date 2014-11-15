Genesis is a toolkit for building worlds programatically. The central functional unit of Genesis is the Map; a map is an arbitrarily sized piece of terrain, which may or may not contain bodies of water, mountain ranges complete with volcanos and caverns, forests, and other natural features. If desired, unnatural structures can be placed, such as cities, dungeons, and other artifical or otherworldly features.

#Installation
##PyPI
This project is available on PyPI and can be installed with `pip`.
````
pip install --user genesis
````
##Manual
You can also manually install this project by cloning it and running setup.py.
````
git clone https://github.com/therealfakemoot/Genesis.git
cd Genesis/
python setup.py install --user
````

#Demo
After installation, a demo is available to showcase simple uses. The simplest invocation looks something like this:
````
genesis --demo X Y
````
For detailed usage instructions, see ````python -m genesis --help````.


##*_WARNING_*
Trying to contour plot a map larger than 1000x1000 may *completely* bomb your memory. Be careful. Start gradually.


#Progress
- [x] Phase One: Height Map Generation and Display
- [ ] Phase Two: Biome Placement
- [ ] Phase Three: Artificial Feature Generation
- [ ] Phase Four: Artifical Feature Placement
