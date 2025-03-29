import pytest
import project

def test_weather_icon():
    assert project.weather_icon("Clear") == "☀️"
    assert project.weather_icon("Clouds") == "☁️"

def test_decide_activity():
    assert project.decide_activity("Clear") == "Go for a walk in the nature"
    assert project.decide_activity("Rain") == "Stay indoors or go shopping"
    
    
def test_decide_clothing():
    assert project.decide_clothing(30) == "Wear shorts and a t-shirt"
    
def test_get_weather_data():
    with pytest.raises(SystemExit):
        project.get_weather_data("Randomcity")