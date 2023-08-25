from temperature_control_unit import TemperatureControlUnit
import pytest
from pytest_bdd import given, when, then, scenario

# Fixture to create a new instance of TemperatureControlUnit for each scenario
@pytest.fixture
def temperature_unit():
    return TemperatureControlUnit()

# Define a pytest-bdd scenario
@scenario("temperature_control.feature", "Initial state is OFF")
def test_initial_state_off():
    pass

# Define steps for the scenario
@given("the temperature control unit is initially OFF")
def initial_state(temperature_unit):
    assert temperature_unit.get_state() == "OFF"

# Define a pytest-bdd scenario
@scenario("temperature_control.feature", "Transition to HEATING")
def test_transition_to_heating():
    pass

# Define steps for the scenario
@given("the temperature control unit is initially OFF")
def initial_state(temperature_unit):
    assert temperature_unit.get_state() == "OFF"

@when("the user selects a coffee brewing option")
def select_brew_option(temperature_unit):
    temperature_unit.select_coffee_brewing_option()

@then("the temperature control unit should transition to HEATING")
def transition_to_heating(temperature_unit):
    assert temperature_unit.get_state() == "HEATING"

# Define a pytest-bdd scenario
@scenario("temperature_control.feature", "Transition to READY")
def test_transition_to_ready():
    pass

# Define steps for the scenario
@given("the temperature control unit is initially OFF")
def initial_state(temperature_unit):
    assert temperature_unit.get_state() == "OFF"

@when("the user selects a coffee brewing option")
def select_brew_option(temperature_unit):
    temperature_unit.select_coffee_brewing_option()

@when("the temperature control unit starts heating")
def start_heating(temperature_unit):
    temperature_unit.start_heating()

@when("the temperature reaches the desired level")
def reach_desired_temperature(temperature_unit):
    temperature_unit.reach_desired_temperature()

@then("the temperature control unit should transition to READY")
def transition_to_ready(temperature_unit):
    assert temperature_unit.get_state() == "READY"
