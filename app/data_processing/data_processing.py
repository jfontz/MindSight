import os
import pandas as pd
import plotly.express as px

from app import app, db
from app.models.models import *
from flask import jsonify
from sqlalchemy.orm import joinedload


def process_data(first_metric, second_metric):
    with app.app_context():
        data = (
            StudentInformation.query
            .options(joinedload(StudentInformation.personal_information))
            .options(joinedload(StudentInformation.family_background))
            .options(joinedload(StudentInformation.health_information))
            .options(joinedload(StudentInformation.educational_background))
            .options(joinedload(StudentInformation.psychological_assessments))
            .all()
        )
        count = 0
        data_list = []
        for record in data:
            personal_information = record.personal_information
            family_background = record.family_background
            health_information = record.health_information
            educational_background = record.educational_background
            psychological_assessments = record.psychological_assessments

            course_name = record.course
            college = Course.query.filter_by(name=course_name).first()
            college_name = college.college.name if college else None 

            data_list.append({
                'student_id': record.student_id,
                'course': course_name,
                'campus': record.campus,
                'gpa': record.gpa,
                'college': college_name,
                'year_level': record.year_level,
                'age': personal_information.age,
                'gender': personal_information.gender,
                'religion': personal_information.religion,
                'nationality': personal_information.nationality,
                'learning_styles': psychological_assessments.learning_styles,
                'personality_test': psychological_assessments.personality_test,
                'iq_test': psychological_assessments.iq_test
            })

        df = pd.DataFrame(data_list)
        data_mean = df.groupby(first_metric)[second_metric].mean().reset_index()
        data_dict = data_mean.to_dict(orient='records')

        return data_dict