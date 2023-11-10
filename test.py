def gnr_reg_shapes(numbers, shape_ty):
  import time
  from typing_extensions import overload
  import cv2
  import numpy as np
  import random
  import matplotlib.pyplot as plt

  # Define
  width = 640
  height = 480

  # Create
  random_image = np.ones((height, width, 3), dtype=np.uint8) * 255 #16

  # Define
  num_shapes = numbers

  # Define
  shape_counts = {
      "Triangle": 0,
      "Square": 0,
      "Pentagon": 0,
      "Hexagon": 0,
      "Heptagon": 0,
      "Octagon": 0,
      "Nonagon": 0,
      "Decagon": 0,
      "Circle": 0
        # Add
    }
  resktor = shape_ty
    # Generate
  for _ in range(num_shapes):


      # Randomy

      shape_type = resktor

      # Random
      color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

      # Random
      x, y = random.randint(0, width-1), random.randint(0, height-1)
      size = random.randint(20, 100)

      if shape_type == 3:  # Triangle
          points = np.array([
              [x, y],
              [x + size, y],
              [x + size // 2, y - int(0.866 * size)]  # Height
          ])
          cv2.fillPoly(random_image, [points], color)
          shape_counts["Triangle"] += 1
      elif shape_type == 4:  # Square
          cv2.rectangle(random_image, (x, y), (x + size, y + size), color, -1)  # -1
          shape_counts["Square"] += 1
      elif shape_type == 5:  # Pentagon
          angle = 360 / 5
          vertices = []
          for i in range(5):
              px = int(x + size * np.cos(np.radians(i * angle)))
              py = int(y + size * np.sin(np.radians(i * angle)))
              vertices.append([px, py])
          points = np.array(vertices)
          cv2.fillPoly(random_image, [points], color)
          shape_counts["Pentagon"] += 1
      elif shape_type == 6:  # Hexagon
          angle = 360 / 6
          vertices = []
          for i in range(6):
              px = int(x + size * np.cos(np.radians(i * angle)))
              py = int(y + size * np.sin(np.radians(i * angle)))
              vertices.append([px, py])
          points = np.array(vertices)
          cv2.fillPoly(random_image, [points], color)
          shape_counts["Hexagon"] += 1
      elif shape_type == 7:  # Heptagon
          angle = 360 / 7
          vertices = []
          for i in range(7):
              px = int(x + size * np.cos(np.radians(i * angle)))
              py = int(y + size * np.sin(np.radians(i * angle)))
              vertices.append([px, py])
          points = np.array(vertices)
          cv2.fillPoly(random_image, [points], color)
          shape_counts["Heptagon"] += 1
      elif shape_type == 8:  # Octagon
          angle = 360 / 8
          vertices = []
          for i in range(8):
              px = int(x + size * np.cos(np.radians(i * angle)))
              py = int(y + size * np.sin(np.radians(i * angle)))
              vertices.append([px, py])
          points = np.array(vertices)
          cv2.fillPoly(random_image, [points], color)
          shape_counts["Octagon"] += 1
      elif shape_type == 9:  # Nonagon
          angle = 360 / 9
          vertices = []
          for i in range(9):
              px = int(x + size * np.cos(np.radians(i * angle)))
              py = int(y + size * np.sin(np.radians(i * angle)))
              vertices.append([px, py])
          points = np.array(vertices)
          cv2.fillPoly(random_image, [points], color)
          shape_counts["Nonagon"] += 1
      elif shape_type == 10:  #Decagon
          angle = 360 / 10
          vertices = []
          for i in range(10):
              px = int(x + size * np.cos(np.radians(i * angle)))
              py = int(y + size * np.sin(np.radians(i * angle)))
              vertices.append([px, py])
          points = np.array(vertices)
          cv2.fillPoly(random_image, [points], color)
          shape_counts["Decagon"] += 1
      elif shape_type == 11:  #circle
          cv2.circle(random_image, (x, y), size // 2, color, -1)  # -1 fills the circle
          shape_counts["Circle"] += 1

      else:
          raise KeyError(f"""are you dumb? Y
          yes of course. '_'       """)
      # Display the random image using Matplotlib
      plt.imshow(random_image)
      plt.axis('off')  # Turn off axis labels



  plt.show()    # Print the counts of each shape
  for shape, count in shape_counts.items():
      print(f"{shape}: {count}")
  #if overload:
