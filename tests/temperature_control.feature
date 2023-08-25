Feature: Temperature Control Unit Behavior

  Scenario: Initial state is OFF
    Given the temperature control unit is initially OFF

  Scenario: Transition to HEATING
    Given the temperature control unit is initially OFF
    When the user selects a coffee brewing option
    Then the temperature control unit should transition to HEATING

  Scenario: Transition to READY
    Given the temperature control unit is initially OFF 
    When  the user selects a coffee brewing option And the temperature control unit in HEATING state And the temperature is reash  
    Then the temperature control unit should transition to READY

  Scenario: Transition HEATING to READY
    Given the temperature control unit in HEATING state
    When the temperature is reash  
    Then the temperature control unit should transition to READY

 Scenario: Transition in  HEATING 
    Given the temperature control unit in HEATING state
    When the temperature not  reash to the disire temperature 
    Then the temperature control unit should not change to ready state
