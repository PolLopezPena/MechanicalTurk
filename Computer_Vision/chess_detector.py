import cv2
import torch
import numpy as np


# Cargar el modelo YOLOv5
def load_yolo_model(model_path):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
    return model


# Detectar piezas de ajedrez en la imagen
def detect_chess_pieces(model, image_path):
    img = cv2.imread(image_path)
    results = model(img)
    return results, img


# Extraer y convertir coordenadas y etiquetas
def extract_detections(results, img_shape):
    labels, coords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    detections = []
    height, width = img_shape[:2]
    for i in range(len(labels)):
        x1, y1, x2, y2, conf = coords[i]
        label = int(labels[i])
        # Convertir las coordenadas de proporciones a píxeles
        x1, y1, x2, y2 = int(x1 * width), int(y1 * height), int(x2 * width), int(y2 * height)
        detections.append({
            'label': model.names[label],
            'confidence': float(conf),
            'coordinates': (x1, y1, x2, y2)
        })
    return detections


# Filtrar detecciones por color
def filter_detections_by_color(img, detections):
    filtered_detections = []
    for detection in detections:
        x1, y1, x2, y2 = detection['coordinates']
        piece_img = img[y1:y2, x1:x2]

        # Convertir la imagen a HSV
        hsv = cv2.cvtColor(piece_img, cv2.COLOR_BGR2HSV)

        # Definir rangos de color para rojo y verde
        lower_red1 = np.array([0, 70, 50])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 70, 50])
        upper_red2 = np.array([180, 255, 255])
        lower_green = np.array([35, 40, 40])
        upper_green = np.array([85, 255, 255])

        # Crear máscaras
        mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.bitwise_or(mask_red1, mask_red2)

        # Verificar si hay suficiente color rojo o verde
        if np.sum(mask_red) > 0 and np.sum(mask_green) > 0:
            # Priorizar verde si ambas máscaras tienen suficientes píxeles
            detection['label'] = 'green'
        elif np.sum(mask_red) > 0:
            detection['label'] = 'red'
        elif np.sum(mask_green) > 0:
            detection['label'] = 'green'

        filtered_detections.append(detection)
    return filtered_detections


# Dibujar las detecciones en la imagen
def draw_detections(img, detections):
    for detection in detections:
        x1, y1, x2, y2 = detection['coordinates']
        label = detection['label']
        conf = detection['confidence']
        color = (0, 255, 0) if label == 'green' else (0, 0, 255)
        # Dibujar el cuadro delimitador y la etiqueta
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    return img


# Detectar el tablero de ajedrez usando el color azul cian del marco
def detect_chess_board(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_cyan = np.array([85, 50, 50])
    upper_cyan = np.array([105, 255, 255])

    mask = cv2.inRange(hsv, lower_cyan, upper_cyan)
    # Aplicar operaciones morfológicas para mejorar la máscara
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return (x, y, x + w, y + h), image
    return None, image


if __name__ == "__main__":
    # Ruta a la imagen del tablero de ajedrez
    image_path = "image/image8.PNG"  # Actualiza esta ruta a la ubicación de tu imagen
    # Ruta al modelo YOLOv5
    model_path = "models/yolo5n_chess_pieces_rg.pt"

    # Cargar el modelo YOLOv5
    model = load_yolo_model(model_path)

    # Detectar las piezas de ajedrez
    results, img = detect_chess_pieces(model, image_path)

    # Extraer y convertir detecciones
    detections = extract_detections(results, img.shape)

    # Filtrar las detecciones por color
    filtered_detections = filter_detections_by_color(img, detections)

    # Dibujar las detecciones en la imagen
    img_with_detections = draw_detections(img, filtered_detections)

    # Detectar el tablero de ajedrez
    board_coords, img_with_board = detect_chess_board(img_with_detections)

    # Mostrar la imagen con las detecciones
    cv2.imshow("Detections", img_with_board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Imprimir las posiciones de las piezas
    for detection in filtered_detections:
        print(detection)

    # Imprimir las coordenadas del tablero
    if board_coords:
        print(f"Tablero de ajedrez detectado en: {board_coords}")
    else:
        print("No se detectó el tablero de ajedrez")
