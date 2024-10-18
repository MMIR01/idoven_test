// URLs
export const website_speed_url = "website-speed"
export const history_url = website_speed_url + "/history"
export const url_speed_test = "https://es.idoven.ai/"
export const invalid_url = "invalid-url"
export const long_url = "http://chart.apis.google.com/chart?chs=500x500&chma=0,0,100,100&cht=p&chco=FF0000%2CFFFF00%7CFF8000%2C00FF00%7C00FF00%2C0000FF&chd=t%3A122%2C42%2C17%2C10%2C8%2C7%2C7%2C7%2C7%2C6%2C6%2C6%2C6%2C5%2C5&chl=122%7C42%7C17%7C10%7C8%7C7%7C7%7C7%7C7%7C6%7C6%7C6%7C6%7C5%7C5&chdl=android%7Cjava%7Cstack-trace%7Cbroadcastreceiver%7Candroid-ndk%7Cuser-agent%7Candroid-webview%7Cwebview%7Cbackground%7Cmultithreading%7Candroid-source%7Csms%7Cadb%7Csollections%7Cactivity|Chart"

// Error messages
export const error_messages =
{
    "empty_url": "Enter a website URL to start the performance test",
    "invalid_url": "URL must include"
}

// Expected elements
export const waiting_result_text = "Waiting In Queue"

export const website_speed_elements =
{ 
    "start_test_text": "Start Test",
    "input_field": "input[name='url']",
    "device_select": "select[name='device']",
    "mobile_option": "Mobile",
    "desktop_option": "Desktop",
    "sign_up_option": "Sign up to test from 20+ test locations",
    "test_history_link": "a",
    "test_history_text": "Test History",
    "view_sample_report_link": "a",
    "view_sample_report_text": "View Sample Report"   
}

export const performance_overall =
{
    "page_title_text": "Page Speed Report",
    "user_score_text": "Real User Score",
    "lab_score_text": "Lab Score"
}

export const performance_metrics_summary =
{
    "good_text": "Good (CrUX)",
    "first_paint_text": "First Contentful Paint",
    "largest_paint_text": "Largest Contentful Paint",
    "cumulative_text": "Cumulative Layout Shift",
    "weight_text": "Page Weight"
}

export const performance_lab_view =
{
    "full_ttfb_text": "Full TTFB",
    "first_paint_text": "First Contentful Paint",
    "largest_paint_text": "Largest Contentful Paint",
    "speed_index_text": "Speed Index",
    "cpu_time_text": "CPU Time",
    "blocking_time_text": "Total Blocking Time",
    "cummulative_text": "Cumulative Layout Shift",
    "weight_text": "Page Weight"
}

export const performance_other_results =
{
    "test_result_text": "Test Result",
    "video_recording_text": "Video Recording",
    "recommendation_text": "Recommendation"
}

export const performance_metrics_vitals =
{
    "first_paint_text": "First Contentful Paint (CrUX)",
    "largest_pain_text": "Largest Contentful Paint (CrUX)",
    "cumulative_text": "Cumulative Layout Shift (CrUX)",
    "interaction_paint_text": "Interaction to Next Paint (CrUX)",
    "first_paint_text2": "First Contentful Paint",
    "largest_paint_text2": "Largest Contentful Paint",
    "cumulative_text2": "Cumulative Layout Shift",
    "total_blocking_text": "Total Blocking Time",
    "time_byte_text": "Time to First Byte (CrUX)",
    "full_ttfb_text": "Full TTFB",
    "rtt_teet": "Round Trip Time (CrUX)",
    "good_text": "Good (CrUX)",
    "largest_paint_text": "Largest Contentful Paint Element",
    "lcp_text": "LCP Development",
    "layout_shift_text": "Layout Shifts"
}

export const performance_lighthouse = 
{
    "light_house_text": "Lighthouse Scores",
    "performance_text": "Performance",
    "accessibility_text": "Accessibility",
    "best_practices_text": "Best Practices",
    "seo_text": "SEO",
    "lighthouse_report_text": "Lighthouse Report",
    "first_contentful_paint_text": "First Contentful Paint",
    "largest_contentful_paint_text": "Largest Contentful Paint",
    "total_blocking_time_text": "Total Blocking Time",
    "cumulative_layout_shift_text": "Cumulative Layout Shift",
    "speed_index_text": "Speed Index",
}

export const performance_sections =
{
    "web_vitals_text": "Web Vitals",
    "requests_text": "Requests",
    "lighthouse_text": "Lighthouse"
}

export const test_history_page =
{
    "main_text": "Site Speed Test History",
    "url_section": "URL",
    "device_section": "Device",
    "date_section": "Date",
    "empty": "run any tests yet."
}