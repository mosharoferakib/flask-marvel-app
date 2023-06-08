from flask import render_template, flash, redirect, url_for, g
from . import bp
from flask_login import current_user, login_required
from app.models import UserCollection, User
from app.forms import CollectionForm




@bp.route('/your_collection', methods=['GET','POST'])
@login_required
def collect_heroes():
    form = CollectionForm()
    if form.validate_on_submit():
        u = UserCollection(name=form.name.data, description=form.description.data, comics_appeared_in=form.comics.data, super_power=form.superpower.data)
        u.user_id = current_user.id
        u.commit()
        flash('Published', 'success')
        return redirect(url_for('social.your_collection', username=current_user.username))
    return render_template('collect_heroes.jinja', form=form)

@bp.route('/userpage/<username>')
@login_required
def your_collection(username):
    user = User.query.filter_by(username=username).first()
    return render_template('your_collection.jinja', title=username, user=user)