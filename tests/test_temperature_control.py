import pytest
from temperature_control_unit import TemperatureControlUnit

# Fixture to create a new instance of TemperatureControlUnit for each test
@pytest.fixture
def temperature_unit():
    return TemperatureControlUnit()

# Scenario 1: Initial state is OFF
def test_initial_state_off(temperature_unit):
    assert temperature_unit.get_state() == "OFF"

# Scenario 2: Transition to HEATING
def test_transition_to_heating(temperature_unit):
    # Implement test code here
    assert temperature_unit.get_state() == "HEATING"

# Scenario 3: Transition to READY
def test_transition_to_ready(temperature_unit):
    # Implement test code here
    assert temperature_unit.get_state() == "READY"

