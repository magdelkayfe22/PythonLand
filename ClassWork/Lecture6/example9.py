# Nested Dictionaries 
nested_dict = {
    'teacher' : {
        'first_name': 'Omar',
        'last_name': 'Ellis'
    },
    'classes': {
        'course': 'ET-574',
        'days_times': {
            'tuesday': '9:10 AM - 10:50 AM',
            'thursday': '9:10 AM - 10:50 AM',
        }
    }
}
print(f"Teacher: {nested_dict['teacher']}")
print(f"Course: {nested_dict['classes']['course']}")
print(f"Schedule: {nested_dict['classes']['days_times']}")