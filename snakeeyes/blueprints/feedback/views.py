from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
    render_template)
from flask_login import current_user

from snakeeyes.blueprints.feedback.forms import FeedbackForm

feedback = Blueprint('feedback', __name__, template_folder='templates')


@feedback.route('/feedback', methods=['GET', 'POST'])
def index():
    # Pre-populate the email field if the user is signed in.
    form = FeedbackForm(obj=current_user)

    if form.validate_on_submit():
        # This prevents circular imports.
        from snakeeyes.blueprints.feedback.tasks import deliver_feedback_email

        deliver_feedback_email.delay(request.form.get('email'), request.form.get('message'))

        flash('Thanks for your feedback!', 'success')
        return redirect(url_for('feedback.index'))

    return render_template('feedback/index.html', form=form)
