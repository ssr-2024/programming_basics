# Lösungen zum Auftrag 2
## Zeitmessungen
Die Zeitmessungen können aufgrund von Hardware, Betriebssysteme, und Systemressourcen variieren.
### Sample: 1'000 
```cmd
Results for 0.001 Mio rows:
time to save data:  0.008370900002773851
Average load_data_time time: Pandas = 0.014449s, Polars = 0.008447s, Speedup = 1.71x
Average join_time time: Pandas = 0.004768s, Polars = 0.002336s, Speedup = 2.04x
Average filter_time time: Pandas = 0.002457s, Polars = 0.001493s, Speedup = 1.65x
Average calc_avg_hr_time time: Pandas = 0.002877s, Polars = 0.003039s, Speedup = 0.95x
Average save_data_time time: Pandas = 0.014376s, Polars = 0.017274s, Speedup = 0.83x
```

### Sample: 10'000 
```cmd
Results for 0.01 Mio rows:
Average load_data_time time: Pandas = 0.044271s, Polars = 0.006886s, Speedup = 6.43x
Average join_time time: Pandas = 0.013774s, Polars = 0.003914s, Speedup = 3.52x
Average filter_time time: Pandas = 0.002572s, Polars = 0.001362s, Speedup = 1.89x
Average calc_avg_hr_time time: Pandas = 0.003312s, Polars = 0.003625s, Speedup = 0.91x
Average save_data_time time: Pandas = 0.024110s, Polars = 0.015943s, Speedup = 1.51x
```
### Sample: 100'000 
```cmd
Results for 0.1 Mio rows:
Average load_data_time time: Pandas = 0.323429s, Polars = 0.024878s, Speedup = 13.00x
Average join_time time: Pandas = 0.152351s, Polars = 0.032525s, Speedup = 4.68x
Average filter_time time: Pandas = 0.012467s, Polars = 0.003495s, Speedup = 3.57x
Average calc_avg_hr_time time: Pandas = 0.015172s, Polars = 0.005204s, Speedup = 2.92x
Average save_data_time time: Pandas = 0.197970s, Polars = 0.017206s, Speedup = 11.51x
```
### Sample: 1 Mio.
```cmd
Results for 1.0 Mio rows:
Average load_data_time time: Pandas = 3.397275s, Polars = 0.116694s, Speedup = 29.11x
Average join_time time: Pandas = 1.419949s, Polars = 0.210381s, Speedup = 6.75x
Average filter_time time: Pandas = 0.080883s, Polars = 0.026522s, Speedup = 3.05x
Average calc_avg_hr_time time: Pandas = 0.125759s, Polars = 0.021601s, Speedup = 5.82x
Average save_data_time time: Pandas = 2.022131s, Polars = 0.074381s, Speedup = 27.19x
```
### Sample: 10 Mio.
```cmd
Results for 10 Mio rows:
Average load_data_time time: Pandas = 32.843971s, Polars = 1.434218s, Speedup = 22.90x
Average join_time time: Pandas = 20.565928s, Polars = 4.365663s, Speedup = 4.71x
Average filter_time time: Pandas = 0.776050s, Polars = 0.411434s, Speedup = 1.89x
Average calc_avg_hr_time time: Pandas = 1.153208s, Polars = 0.341797s, Speedup = 3.37x
Average save_data_time time: Pandas = 20.022792s, Polars = 0.709820s, Speedup = 28.21x
```
## Beantwortung der Fragen
### Hat die Grösse des Datensatzes einen Einfluss auf das Geschwindigkeitsverhältnis zwischen den beiden Packages?

Ja, die Grösse des Datensatzes hat einen erheblichen Einfluss auf das Geschwindigkeitsverhältnis zwischen Polars und Pandas. Vor allem das Laden und Speichern des Datensatzes wird mit Polars bei grossen Datensätzen vielfach schneller als mit Pandas.

### Welche Funktionen sind in polars optimiert?

1. **Filter-Operationen**: Polars verwendet optimierte Algorithmen, um Filter-Operationen schneller durchzuführen.
2. **Gruppierung und Aggregation**: Polars kann Gruppierungs- und Aggregationsoperationen effizienter ausführen, insbesondere bei großen Datensätzen.
3. **Joins**: Polars bietet optimierte Join-Operationen, die schneller und speichereffizienter sind.
4. **Parallele Verarbeitung**: Polars nutzt die parallele Verarbeitung, um Operationen auf mehreren Kernen gleichzeitig auszuführen.
5. **Speicherverwaltung**: Polars verwendet speichereffiziente Datenstrukturen und Algorithmen, um den Speicherverbrauch zu minimieren und die Leistung zu maximieren.

### Wieso könnte das sein?
Polars ist in Rust geschrieben, einer Systemsprache, die für ihre hohe Leistung und Effizienz bekannt ist. Rust ermöglicht eine bessere Kontrolle über die Speicherverwaltung und die Nutzung von Systemressourcen, was zu einer schnelleren und effizienteren Datenverarbeitung führt. Darüber hinaus nutzt Polars moderne Optimierungstechniken wie Parallelverarbeitung und speichereffiziente Algorithmen, die speziell für die Verarbeitung großer Datenmengen entwickelt wurden. Diese Faktoren tragen dazu bei, dass Polars bei großen Datensätzen deutlich schneller und effizienter ist als Pandas, das in Python geschrieben ist und weniger Kontrolle über die zugrunde liegenden Systemressourcen bietet.