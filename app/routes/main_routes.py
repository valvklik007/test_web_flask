from flask import Blueprint, render_template, request, flash, make_response, Response
from app.forms.city_form import CityForm
from app.services.weather_service import WeatherService
from app.models.history import SearchHistory
from app import db
from sqlalchemy import func
import json

main_bp = Blueprint('weather', __name__)

weather_service = WeatherService()


@main_bp.route('/history')
def history():
    searches = SearchHistory.query.filter(SearchHistory.user_ip == request.remote_addr).order_by(SearchHistory.timestamp.desc()).limit(20).all()
    return render_template('weather/history.html', searches=searches)


@main_bp.route('/api/stats')
def stats():
    result = db.session.query(
        SearchHistory.city,
        func.count(SearchHistory.city).label('count')
    ).group_by(SearchHistory.city).order_by(func.count(SearchHistory.city).desc()).all()

    json_data = []
    for city, count in result:
        json_data.append({"city": city, "count": count})

    return Response(
        json.dumps(json_data, ensure_ascii=False),
        content_type='application/json; charset=utf-8'
    )


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = CityForm()
    weather = None
    last_city  = request.cookies.get('last_city')
    if form.validate_on_submit():
        city = form.city.data.strip().title()
        weather = weather_service.getOneDayForecast(city)
        if not weather:
            flash('Город не найден или ошибка при получении данных.', 'danger')
            return render_template('weather/index.html', form=form)

        user_ip = request.remote_addr
        db.session.add(SearchHistory(city=city, user_ip=user_ip))
        db.session.commit()

        response = make_response(render_template('weather/index.html', form=form, weather=weather, city=city))
        response.set_cookie('last_city', city, max_age=60*60*24*7)
        return response

    return render_template('weather/index.html', form=form, weather=weather, last_city=last_city)


