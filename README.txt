python3 -m dev -i dev/seed-data/test.csv -o vietnam_provinces/data/flat-vehicle.json -f flat-json
python3 -m dev -i dev/seed-data/test.csv -o vietnam_provinces/data/nested-vehicle.json

python3 -m dev -i dev/seed-data/Xa_2021-02-03.csv -o vietnam_provinces/data/flat_province.json -f flat-json
python3 -m dev -i dev/seed-data/Xa_2021-02-03.csv -o vietnam_provinces/data/nested_province.json

python3 -m dev -i dev/seed-data/motor_list_v1.2.csv -o vietnam_provinces/data/flat_motor.json -f flat-json
python3 -m dev -i dev/seed-data/motor_list_v1.2.csv -o vietnam_provinces/data/nested_motor.json

python3 -m dev -i dev/seed-data/motor_list_v1.3.csv -o vietnam_provinces/data/flat_motor_1.3.json -f flat-json
python3 -m dev -i dev/seed-data/motor_list_v1.3.csv -o vietnam_provinces/data/nested_motor_1.3.json