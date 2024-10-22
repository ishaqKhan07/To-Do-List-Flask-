from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from app import db
from app.models import Assessment
from app.forms import AssessmentForm
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    assessments = Assessment.query.all()
    return render_template('index.html', assessments=assessments)

@main.route('/add', methods=['GET', 'POST'])
def add():
    form = AssessmentForm()
    if form.validate_on_submit():
        new_assessment = Assessment(
            title=form.title.data,
            module_code=form.module_code.data,
            deadline=form.deadline.data,
            description=form.description.data,
            completed=form.completed.data
        )
        db.session.add(new_assessment)
        db.session.commit()
        flash('Assessment added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('form.html', form=form)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    assessment = Assessment.query.get_or_404(id)
    form = AssessmentForm(obj=assessment)
    if form.validate_on_submit():
        assessment.title = form.title.data
        assessment.module_code = form.module_code.data
        assessment.deadline = form.deadline.data
        assessment.description = form.description.data
        assessment.completed = form.completed.data
        db.session.commit()
        flash('Assessment updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('form.html', form=form, edit=True)

@main.route('/details/<int:id>')
def details(id):
    assessment = Assessment.query.get_or_404(id)
    return render_template('details.html', assessment=assessment)

@main.route('/mark_complete/<int:id>')
def mark_complete(id):
    assessment = Assessment.query.get_or_404(id)
    assessment.completed = True
    db.session.commit()
    flash('Assessment marked as complete!', 'success')
    return redirect(url_for('main.index'))

@main.route('/delete_assessment/<int:id>')
def delete_assessment(id):
    assessment = Assessment.query.get_or_404(id)
    db.session.delete(assessment)
    db.session.commit()
    flash('Assessment deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/get_assessment_details', methods=['POST'])
def get_details():
    assessment_id = request.form.get('assessment_id')
    details = Assessment.query.get_or_404(assessment_id)
    return jsonify({
        'assessment': {
            'title': details.title,
            'module_code': details.module_code,
            'deadline': details.deadline.strftime('%Y-%m-%d'),
            'description': details.description,
            'completed': details.completed
        }
    })

@main.route('/incomplete')
def incomplete():
    assessments = Assessment.query.filter_by(completed=False).all()
    return render_template('index.html', assessments=assessments)

@main.route('/complete')
def complete():
    assessments = Assessment.query.filter_by(completed=True).all()
    return render_template('index.html', assessments=assessments)
