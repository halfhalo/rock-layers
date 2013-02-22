#/bin/sh
MACH=$1
if [ -z "$1" ]
then
MACH="rock"
fi
echo 'git clone git://github.com/halfhalo/build-webos.git'
echo `git clone git://github.com/halfhalo/build-webos.git`
echo 'cd build-webos'
echo 'git checkout remote-layers'
echo `cd build-webos && git checkout remote-layers`
echo "./mcf -p0 -b0 -r https://raw.github.com/halfhalo/rock-layers/master/weboslayers.py $MACH"
echo `cd build-webos && ./mcf -p0 -b0 -r https://raw.github.com/halfhalo/rock-layers/envy/oe-core-uefi/weboslayers.py $MACH`
cd build-webos
echo "To build, just type make webos-image"