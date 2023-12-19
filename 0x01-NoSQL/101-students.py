#!/usr/bin/env python3
'''
script that returns all students sorted by average score
'''


def top_students(mongo_collection):
    '''
    returns all students sorted by average score
    '''
    student_data = []
    
    for student in mongo_collection.find():
        student_id = student.get('_id')
        name = student.get('name')
        topics = student.get('topics', [])
        
        total_score = sum(topic.get('score', 0) for topic in topics)
        average_score = total_score / len(topics) if topics else 0
        
        student_data.append({
            '_id': student_id,
            'name': name,
            'averageScore': average_score
        })
    
    sorted_students = sorted(student_data, key=lambda x: x['averageScore'], reverse=True)
    
    return sorted_students