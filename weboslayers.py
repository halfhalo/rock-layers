# Copyright (c) 2008 - 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Documentation:
#
# This implementation introduces next generation build environment
# for OpenWebos. The change introduces a mechanism to add additional
# layers to the base ones, meta-webos, meta-oe and oe-core.
# The new layers contribute to the image content of WebOS.
#
# The base layers are defined in weboslayers.py file located in 
# the build directory, i.e build-webos.  Additional layers can
# be added to the same file.
#
# weboslayers.py file format uses python data structures to define 
# the following:
#
# ('layer-name', integer-priority, 'URL', 'submission', 'working-dir')
#
# layers name = uniqe identifier, It represents the layer directoy containing
#               conf/layer.conf.
# priority    = layer priority as defined by Openembedded. Larger numbers
#               have higher priority. A value of -1 indicates that the content
#               is not a layer, for example the bitbake directory.
# URL         = The git repo address for the layer on the web. A value of ''
#               skips the download.
# submission  = Is the git information to download and identify the precise
#               content.  Submssion values could be "branch=<name>" and 
#               "commmit=<id>" or "tag=<label>". Omitted branch information
#               means master. Omitted commit or tag means tip of branch.
# working-dir = Alternative project directory for the layer.
#
# The priority in this file overrides those specified in conf/layer.conf
# for each layer. Excptions are oe-core and meta-oe, where they are present 
# to control downloading of particular version of these layers, the layer priority
# for these two layers must not be changed 
#
# In additon to layers, the distribution name is also defined in this file as well.
#
Distribution = "webos"

# github.com/openembedded repositories are read-only mirrors 
# of authoritative repositories on git.openembedded.org
webos_layers = [
#Pulling from head purely for colors.
('bitbake',          -1, 'git://github.com/openembedded/bitbake.git',        'branch=1.16',  ''  ),
#We are pulling from HEAD instead of a fixed commit due to this: https://github.com/openembedded/oe-core/commit/3fc5923b4c8e99fe22e10fb52181c951330a12f2
('meta',              5, 'git://github.com/openembedded/oe-core.git',        'branch=danny', ''  ),
('meta-oe',           6, 'git://github.com/openembedded/meta-oe.git',        'branch=danny', ''  ),
#meta-intel contains both meta-sugarbay and meta-cedartrail in it, so we have to do some finangling with them to get everything to properly load
('meta-intel',        5, 'git://git.yoctoproject.org/meta-intel.git',        'branch=danny', ''  ),
('meta-sugarbay',     7, '',                                                 '',                         '@CWD@/meta-intel/meta-sugarbay' ),
('meta-cedartrail',   7, '','','@CWD@/meta-intel/meta-cedartrail'),
('meta-webos',       10, 'git://github.com/openwebos/meta-webos.git',        'commit=HEAD', '' ),
#We pull in meta-java for llvm, which is soley used for mesa-dri currently
('meta-java',   10, 'git://github.com/woglinde/meta-java.git',        'branch=master', ''  )
#We want the latest and greatest mesa and friends, so we pull in a layer only containing them
('meta-mesa-upstream',   12, 'git://github.com/halfhalo/meta-mesa-upstream.git','branch=master', ''  ),
#meta-rock contains both meta-slate and meta-envy at the moment, so also having to finangle them.
('meta-rock',        15, 'git://github.com/webOS-ports/meta-rock.git','branch=halfhalo/refactor',    ''  ),
('meta-slate',       16, '','','@CWD@/meta-rock/meta-slate'),
('meta-envy',       16, '','','@CWD@/meta-rock/meta-envy'),
#('meta-networking',   6, 'git://github.com/openembedded/meta-oe.git',        '', ''  ),
#('meta-oe',           6, 'git://github.com/openwebos/meta-oe.git' ,          'commit=5c40f0e', ''),
#('meta-name',        15, '',  '', '/home/userid/meta-name'),

]