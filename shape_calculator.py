class Rectangle:
  def __init__(self, width:int, height:int):
    self.height = height
    self.width = width

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2*self.height + 2*self.width

  def get_diagonal(self):
    return (self.height**2 + self.width**2)**0.5
  
  #@width.setter
  def set_width(self, width):
    self.width = width
  
  #@height.setter
  def set_height(self, height):
    self.height = height

  def __str__(self) -> str:
    return f"Rectangle(width={self.width}, height={self.height})"

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*"*self.width + "\n"
      return picture

  def get_amount_inside(self, shape):
    return int(self.height/shape.height) * int(self.width/shape.width)


class Square(Rectangle):
  def __init__(self, side:int):
    super().__init__(side, side)

  def set_side(self, side):
    self.width = side
    self.height = side
 
  #@width.setter
  def set_width(self, width):
    self.width = width
    self.height = width

#@height.setter
  def set_height(self, height):
    self.width = height
    self.height = height

  def __str__(self) -> str:
    return f"Square(side={self.height})"
