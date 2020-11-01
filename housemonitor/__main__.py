from housemonitor.detect_platform_pi import pi_version
if pi_version():
    from housemonitor.pi_get_humtemp import get_humtemp
else:
    from housemonitor.simulate_get_humtemp import get_humtemp

temp, humidity = get_humtemp()

print(f"Temperature = {str(temp)}")
print(f"Humidity = {str(humidity)}")
