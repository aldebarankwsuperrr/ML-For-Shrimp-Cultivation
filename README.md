
# Shrimp

Api for average weight forecasting and revenue forecasting

## Installation

Install my-project with npm

```bash
  pip install -r requirements.txt
```

## Deployment

To deploy this project run

```bash
  uvicorn app:app
```

## API Reference

### average weight forecasting

```http
  POST http://127.0.0.1:8000/predict/weight
```
#### Parameters
| Parameter | Type     |
| :-------- | :------- |
| `tray_number` | `float` |
| `quantity` | `float` |
| `fasting` | `float` |

#### Usage/Examples

```json
{
    "tray_number": 6.0,
    "quantity": 420.40,
    "fasting": 1.0
}
```



### revenue forecasting

```http
  POST http://127.0.0.1:8000/predict/revenue
```
#### Parameters
| Parameter | Type     |
| :-------- | :------- |
| `size` | `float` |
| `weight` | `float` |
| `number_of_shrimp` | `float` |

#### Usage/Examples
```json
{
    "size": 	300.00,
    "weight": 46.00,
    "number_of_shrimp": 13800.0
}
```
