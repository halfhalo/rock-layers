Distribution = "webos"

webos_layers = [
('bitbake',          -1, 'git://github.com/openembedded/bitbake.git',        'branch=1.16,commit=34a8d45', ''  ),
('meta',              5, 'git://github.com/openembedded/oe-core.git',        'branch=danny,commit=8e057a5', ''  ),
('meta-oe',           6, 'git://github.com/openembedded/meta-oe.git',        'branch=danny,commit=f026e96', ''  ),
#('meta-networking',   6, 'git://github.com/openembedded/meta-oe.git',        '', ''  ),
#('meta-oe',           6, 'git@github.com:openwebos/meta-oe.git' ,            'branch=preview,commit=187c487', ''),
('meta-webos',       10, 'git://github.com/openwebos/meta-webos.git',          'branch=preview', ''),
('meta-intel',       5, 'git://git.yoctoproject.org/meta-intel.git',          'branch=danny', ''),
#('meta-name',        15, '',  '', '/home/userid/meta-name'),
]