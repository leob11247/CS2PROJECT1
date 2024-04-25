from PIL import Image
import os

class ImageEditer:
    def open(self, paths: str) -> Image:
        """
        Method to open image file
        
        :param path: where the image is
        
        :return: opened image
        """
        if not isinstance(paths, list):
            paths = [paths]
        results = [Image.open(path) for path in paths]

        return results if len(paths)!=1 else results[0]
    
    def save(self, image: Image, path: str) -> None:
        """
        Method to save image
        
        :param image: image you'd like to save
        :param path: where to save
        """
        image.save(path)
    
    def remove(self, path: str) -> None:
        """
        Method to delete image
        
        :param path: path to the image to be removed
        """
        os.remove(path)
    
    def resizeByWidth(self, images: list[Image.Image], width: int) -> list[Image.Image]:
        """
        Method to resize an image to a specified width while preserving the aspect ratio
        
        :param images: images to be resized
        :param width: width after resized
        
        :return: resized images
        """
        if not isinstance(images, list):
            images = [images]
            
        results = []
        
        for image in images:
            original_width, original_height = image.size
            new_width = width
            new_height = int(original_height * (new_width / original_width))
            resized_image = image.resize((new_width, new_height))
            results.append(resized_image)

        return results if len(images)!=1 else results[0]
    
    def resizeByHeight(self, images: list[Image.Image], height: int) -> list[Image.Image]:
        """
        Method to resize an image to a specified height while preserving the aspect ratio
        
        :param images: images to be resized
        :param height: height after resized
        
        :return: resized images
        """
        if not isinstance(images, list):
            images = [images]
            
        results = []
        
        for image in images:
            original_width, original_height = image.size
            new_height = height
            new_width = int(original_width * (new_height / original_height))
            resized_image = image.resize((new_width, new_height))
            results.append(resized_image)

        return results if len(images)!=1 else results[0]
