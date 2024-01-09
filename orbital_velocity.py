# orbital_velocity
# by Chris Y. Taylor
# calculates the orbital velocity needed to attain Earth orbits based on
# launch latitude, orbit inclination, orbit height, and
# eccentricity.  Could be modified for other launches from other
# celestial bodies by changing GRAV_PARAMETER,
# (G times planetary body mass, units are ft^3/s^2),
# PLANET_ROTATION (radians/s), and PLANET_RADIUS (n.miles)
# Launch azimuth correction for rotating Earth assumed negligible
# !requires Python math package to function!

GRAV_PARAMETER = 1.41e16
PLANET_ROTATION = 7.2921e-5
PLANET_RADIUS = 3440
RADIANS = 57.29578
# above 3 values are currently set at Earth normal
bad_input = True  #not really bad yet, just nothing entered at this point
while bad_input == True:
    perigee = float(input("What is orbital Perigee altitude in n.miles? "))
    eccentricity = float(input("What is orbital eccentricity? "))
    inclination = float(input("What is orbital inclination in degrees? "))
    latitude = float(input("What launch site latitude in degrees? "))
    # ETR=28.5, WTR=34.6, Wallops=37.85, Woomera=-31.12
    if inclination >= 0 and inclination <= 180 and latitude >=-90 and latitude <=90 and perigee > 0 and eccentricity >= 0 and eccentricity <1:
        bad_input = False
    else:
        print ("Perigee must be positive.")
        print ("Eccentricity must be >=0 and <1")
        print ("Inclination must be from 0 to 180.")
        print ("Latitude must be from -90 to 90.")
site_velocity = PLANET_ROTATION*PLANET_RADIUS*math.cos(abs(latitude/RADIANS))*6076.11549
print ("Velocity contribution of launch site in ft/s is:")
print (site_velocity)
periapsis = PLANET_RADIUS+perigee
apoapsis = (-periapsis-(eccentricity*periapsis))/(eccentricity-1)
semimajor_axis = (periapsis+apoapsis)/2
apogee = apoapsis-PLANET_RADIUS
azumith = RADIANS*math.asin(math.cos(inclination/RADIANS)/math.cos(latitude/RADIANS))
# measuring clockwise with due East as 90 degrees
print ("Launch Azimuth should be: ")
print (azumith)
periapsis_velocity = math.sqrt((2*GRAV_PARAMETER/(periapsis*6076.11549))-(GRAV_PARAMETER/(semimajor_axis*6076.11549)))
print ("Velocity at Perigee in ft/s is: ")
print (periapsis_velocity)
vehicle_velocity = periapsis_velocity-site_velocity
print ("Perigee Velocity contribution from launch vehicle in ft/s is: ")
print (vehicle_velocity)
