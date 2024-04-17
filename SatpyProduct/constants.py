from utils import generate24HourTimeRange,generateDayTimeRange ,generateNightTimeRange

day_and_night_products = [
    { "product_key": "dust"                        ,"product_title": 'Dust_RGB'                                               , "product_type": 'product' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "natural_color_with_night_ir" ,"product_title": 'Picture_4_NaturL_COLOR_rgb_ir016_VIS008_vis006_WG'      , "product_type": 'product' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "airmass"                     ,"product_title": 'Picture_3_Water_vapour_content_IO_region_reprojected_WG', "product_type": 'product' , "valid_time_args": generate24HourTimeRange()},
]

day_products = [
    { "product_key": "fog"                      ,"product_title": 'Fog'              , "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "hrv_fog"                  ,"product_title": 'HRV_Fog'          , "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "snow"                     ,"product_title": 'Snow_RGB'         , "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "hrv_severe_storms_masked" ,"product_title": 'HRV_Severe_Storms', "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "day_microphysics"         ,"product_title": 'Microphysics'     , "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "ir_sandwich"              ,"product_title": 'ir_sandwich'      , "product_type": 'product' , "valid_time_args": generateDayTimeRange()},
    { "product_key": "cloud_phase_distinction"  ,"product_title": 'Cloud_Phase_Distinction'      , "product_type": 'product' , "valid_time_args": generateDayTimeRange()},

]

night_products = [
    { "product_key": "night_fog"          ,"product_title": 'Fog'         , "product_type": 'product' , "valid_time_args": generateNightTimeRange()},
    { "product_key": "night_microphysics" ,"product_title": 'Microphysics', "product_type": 'product' , "valid_time_args": generateNightTimeRange()},
]

band_products = [
    # { "product_key": "HRV"    ,"product_title": 'HRV_IO_region_WG'   , "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "IR_016" ,"product_title": 'IR_016_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "IR_039" ,"product_title": 'IR_039_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "IR_087" ,"product_title": 'IR_087_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "IR_097" ,"product_title": 'IR_097_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "IR_108" ,"product_title": 'IR_108_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "IR_120" ,"product_title": 'IR_120_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "IR_134" ,"product_title": 'IR_134_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "VIS006" ,"product_title": 'VIS_006_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "VIS008" ,"product_title": 'VIS_008_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "WV_062" ,"product_title": 'WV_062_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},
    # { "product_key": "WV_073" ,"product_title": 'WV_073_IO_region_reprojected_WG', "product_type": 'band' , "valid_time_args": generate24HourTimeRange()},

]

products=  band_products + day_and_night_products + night_products + day_products;
    
export = products