UIList = []
tab = {}
UIList.append(tab)
tab['name'] = 'common'
tab['entries'] = []
entry = {}
entry['name'] = 'None'
entry['type'] = 'frame'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'white_point'
entry['type'] = 'enum'
entry['displayName'] = 'White Point'
entry['default'] = 'D50'
entry['addInfo'] = 'User:A:B:C:D50:D55:D65:D75:E:F1:F2:F3:F4:F5:F6:F7:F8:F9:F10:F11:F12'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'white_pointX'
entry['type'] = 'float'
entry['displayName'] = 'White Point X'
entry['default'] = '0.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'white_pointY'
entry['type'] = 'float'
entry['displayName'] = 'White Point Y'
entry['default'] = '0.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'bih_tri_threshold'
entry['type'] = 'int'
entry['displayName'] = 'BIH Threshold'
entry['default'] = '1100000'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'metropolis'
entry['type'] = 'bool'
entry['displayName'] = 'Metropolis'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'large_mutation_prob'
entry['type'] = 'float'
entry['displayName'] = 'Large Mutation Probability'
entry['default'] = '0.1'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'max_change'
entry['type'] = 'float'
entry['displayName'] = 'Perturb Radius'
entry['default'] = '.01'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'max_num_consec_rejections'
entry['type'] = 'int'
entry['displayName'] = 'Number of Rejections'
entry['default'] = '1000'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'logging'
entry['type'] = 'bool'
entry['displayName'] = 'Logging'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'path_tracing'
entry['type'] = 'enum'
entry['displayName'] = 'Path Tracing'
entry['default'] = '0'
entry['addInfo'] = 'bidirectional:backwards'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_mapper'
entry['type'] = 'enum'
entry['displayName'] = 'Tone Mapper'
entry['default'] = '1'
entry['addInfo'] = 'linear:reinhard:camera'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_linearScale'
entry['type'] = 'float'
entry['displayName'] = 'Scale'
entry['default'] = '1.0'
entry['addInfo'] = 'minmax:0.0001:100'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_reinhardPreScale'
entry['type'] = 'float'
entry['displayName'] = 'Pre Scale'
entry['default'] = '1.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_reinhardPostScale'
entry['type'] = 'float'
entry['displayName'] = 'Post Scale'
entry['default'] = '1.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_reinhardBurn'
entry['type'] = 'float'
entry['displayName'] = 'Burn'
entry['default'] = '10.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_cameraResponse_function_path'
entry['type'] = 'string'
entry['displayName'] = 'Response Func File'
entry['default'] = '""'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_cameraEv_adjust'
entry['type'] = 'float'
entry['displayName'] = 'EV Adjust'
entry['default'] = '0.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'tone_cameraFilm_iso'
entry['type'] = 'float'
entry['displayName'] = 'ISO'
entry['default'] = '200.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'save_untonemapped_exr'
entry['type'] = 'bool'
entry['displayName'] = 'Untonemapped EXR'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'save_tonemapped_exr'
entry['type'] = 'bool'
entry['displayName'] = 'Tonemapped EXR'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'save_igi'
entry['type'] = 'bool'
entry['displayName'] = 'Save Indigo ImageFile'
entry['default'] = 'false'
entry['addInfo'] = ''
tab['entries'].append(entry)
entry = {}
entry['name'] = 'image_save_period'
entry['type'] = 'float'
entry['displayName'] = 'Img Save Period'
entry['default'] = '60'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'halt_time'
entry['type'] = 'float'
entry['displayName'] = 'Halt Time'
entry['default'] = '-1'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'halt_samples_per_pixel'
entry['type'] = 'int'
entry['displayName'] = 'Max Samples PP'
entry['default'] = '-1'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'hybrid'
entry['type'] = 'bool'
entry['displayName'] = 'Hybrid Sampling'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'None'
entry['type'] = 'frame'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'auto_choose_num_threads'
entry['type'] = 'bool'
entry['displayName'] = 'Auto Choose Threads'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'num_threads'
entry['type'] = 'bool'
entry['displayName'] = 'Num Threads'
entry['default'] = '1'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'super_sample_factor'
entry['type'] = 'int'
entry['displayName'] = 'Supersampling'
entry['default'] = '2'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'watermark'
entry['type'] = 'bool'
entry['displayName'] = 'Watermark'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'info_overlay'
entry['type'] = 'bool'
entry['displayName'] = 'Info Overlay'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'cache_trees'
entry['type'] = 'bool'
entry['displayName'] = 'Cache Kd-Trees'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'aperture_diffraction'
entry['type'] = 'bool'
entry['displayName'] = 'Aperture Diffraction'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'post_process_diffraction'
entry['type'] = 'bool'
entry['displayName'] = 'Post Aperture Diffraction'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'render_foreground_alpha'
entry['type'] = 'bool'
entry['displayName'] = 'Alpha Image'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'splat_filter'
entry['type'] = 'enum'
entry['displayName'] = 'Splat Filter'
entry['default'] = '0'
entry['addInfo'] = 'fastbox:radial:mn_cubic'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'splat_filter_cubic_b'
entry['type'] = 'float'
entry['displayName'] = 'Cubic Splat B'
entry['default'] = '0.6'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'splat_filter_cubic_ring'
entry['type'] = 'float'
entry['displayName'] = 'Cubic Splat Ring'
entry['default'] = '0.2'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'downsize_filter'
entry['type'] = 'enum'
entry['displayName'] = 'Downsize Filter'
entry['default'] = '0'
entry['addInfo'] = 'mn_cubic:gauss:sharp'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'downsize_filter_cubic_radius'
entry['type'] = 'float'
entry['displayName'] = 'Cubic DS Radius'
entry['default'] = '2'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'vignetting'
entry['type'] = 'bool'
entry['displayName'] = 'Vignetting'
entry['default'] = 'true'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'gpu'
entry['type'] = 'bool'
entry['displayName'] = 'GPU Acceleration'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'selected_gpu_device'
entry['type'] = 'enum'
entry['displayName'] = 'GPU Device'
entry['default'] = '0'
entry['addInfo'] = 'CUDA:OPEN_CL'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'glass_acceleration'
entry['type'] = 'bool'
entry['displayName'] = 'Glass Accerlation'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'None'
entry['type'] = 'frame'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'environmentType'
entry['type'] = 'enum'
entry['displayName'] = 'Environment Type'
entry['default'] = '1'
entry['addInfo'] = 'Off:Color/Map:Sun'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'environmentColor'
entry['type'] = 'color'
entry['displayName'] = 'Environment Color'
entry['default'] = '0.4:0.4:1.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'environmentSun'
entry['type'] = 'message'
entry['displayName'] = 'Environment Sun'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'turbidity'
entry['type'] = 'float'
entry['displayName'] = 'Sky Turbidity'
entry['default'] = '2.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'extra_atmospheric'
entry['type'] = 'bool'
entry['displayName'] = 'Extra Athmospheric'
entry['default'] = 'false'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'sun_layer'
entry['type'] = 'int'
entry['displayName'] = 'Sun Layer'
entry['default'] = '0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'sky_layer'
entry['type'] = 'int'
entry['displayName'] = 'Sky Layer'
entry['default'] = '0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'sky_model'
entry['type'] = 'enum'
entry['displayName'] = 'Sky Model'
entry['default'] = '0'
entry['addInfo'] = 'original:captured-simulation'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'environmentMapType'
entry['type'] = 'enum'
entry['displayName'] = 'Environ Map Type'
entry['default'] = '0'
entry['addInfo'] = 'Spherical:Lat-Long'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'environmentMapMultiplier'
entry['type'] = 'float'
entry['displayName'] = 'Map Multiplier'
entry['default'] = '1.0'
tab['entries'].append(entry)
entry = {}
entry['name'] = 'preferredTextEditor'
entry['type'] = 'string'
entry['displayName'] = 'Text Editor'
entry['default'] = 'notepad.exe'
tab['entries'].append(entry)
