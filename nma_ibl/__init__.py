import datajoint as dj

reference = dj.create_virtual_module('reference', 'ibl_reference')
subject = dj.create_virtual_module('subject', 'ibl_subject')
action = dj.create_virtual_module('action', 'ibl_action')
acquisition = dj.create_virtual_module('acquisition', 'ibl_acquisition')
data = dj.create_virtual_module('data', 'ibl_data')
behavior = dj.create_virtual_module('behavior', 'ibl_behavior')
behavior_analyses = dj.create_virtual_module('behavior_analyses', 'ibl_analyses_behavior')
