from utils import is_time_present,generate24HourTimeRange,generateDayTimeRange ,generateNightTimeRange
day_products = [
    'airmass',
    'ash',
    'cloud_phase_distinction',
    'cloud_phase_distinction_raw',
    'cloudtop',
    'cloudtop_daytime',
    'colorized_ir_clouds',
    'convection',
    'day_microphysics',
    'day_microphysics_winter',
    'dust',
    'fog',
    'green_snow',
    'hrv_clouds',
    'hrv_fog',
    'hrv_severe_storms',
    'hrv_severe_storms_masked',
    'ir108_3d',
    'ir_cloud_day',
    'ir_overview',
    'ir_sandwich',
    'natural_color',
    'natural_color_nocorr',
    'natural_color_raw',
    'natural_color_raw_with_night_ir',
    'natural_color_with_night_ir',
    'natural_color_with_night_ir_hires',
    'natural_enh',
    'natural_enh_with_night_ir',
    'natural_enh_with_night_ir_hires',
    'natural_with_night_fog',
    # 'night_fog',
    # 'night_ir_alpha',
    # 'night_ir_with_background',
    # 'night_ir_with_background_hires',
    # 'night_microphysics',
    'overview',
    'overview_raw',
    'realistic_colors',
    'rocket_plume_day',
    'rocket_plume_night',
    'snow',
    'vis_sharpened_ir'
]

night_products = [
    'night_fog',
    'night_ir_alpha',
    'night_ir_with_background',
    'night_ir_with_background_hires',
    'night_microphysics',
]

all_bands=[
    'HRV',
    'IR_016',
    'IR_039',
    'IR_087',
    'IR_097',
    'IR_108',
    'IR_120',
    'IR_134',
    'VIS006',
    'VIS008',
    'WV_062',
    'WV_073',
]



day_products = [
    { "product_key": "fog" ,"product_title": 'Fog', "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
]

night_products = [
    { "product_key": "night_fog" ,"product_title": 'Fog', "product_type": 'product' , "valid_time_args": generateNightTimeRange()},
]

band_products = [
    { "product_key": "HRV" ,"product_title": 'HRV', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_016" ,"product_title": 'IR_016', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_039" ,"product_title": 'IR_039', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_087" ,"product_title": 'IR_087', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_097" ,"product_title": 'IR_097', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_108" ,"product_title": 'IR_108', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_120" ,"product_title": 'IR_120', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "IR_134" ,"product_title": 'IR_134', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "VIS006" ,"product_title": 'VIS006', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "VIS008" ,"product_title": 'VIS008', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "WV_062" ,"product_title": 'WV_062', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    { "product_key": "WV_073" ,"product_title": 'WV_073', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
]

products= band_products + night_products + day_products
    
export = day_products, night_products, all_bands, products