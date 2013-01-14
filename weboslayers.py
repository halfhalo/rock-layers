Distribution = "webos"

webos_layers = [
('bitbake',          -1, 'git://github.com/openembedded/bitbake.git',        'branch=1.16,commit=34a8d45',  ''  ),
('meta',              5, 'git://github.com/openembedded/oe-core.git',        'branch=danny,commit=8e057a5', ''  ),
('meta-oe',           6, 'git://github.com/openembedded/meta-oe.git',        'branch=danny,commit=f026e96', ''  ),
('meta-webos',       10, 'git://github.com/webOS-ports/meta-webos.git',        'branch=webOS-ports/master-next',              ''  ),
('meta-intel',        5, 'git://git.yoctoproject.org/meta-intel.git',        'branch=danny',                ''  ),
('meta-sugarbay',     6, '',                                                 '',                    'meta-intel/meta-sugarbay'),
('meta-rock',        15, 'git://git.github.com/webOS-ports/meta-rock.git',   'branch=halfhalo/refactor',    ''  ),
('meta-slate',       16, '',                                                 '',                    'meta-rock/meta-slate'),
]