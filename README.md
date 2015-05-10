#Image Procecessing in Python

If you are interested in image classification problems, e.g. classifying dog from cat, female from male, etc,
`pyimage` is designed to make image transformations and vectorization easy.

<br>

1. First you need to download images you are interested to classify. By convention, the directory structure is
   such that under the parent directory, there are sub-directories containing images of each of the classes
   you are interested in. [Here](https://www.dropbox.com/s/cg2o5yj5gfj17cl/cat_dog.zip?dl=0)
   is a small dataset <sup>[1]</sup> containing images of cats and dogs. The parent directory is `cat_dog`, and the
   sub-directories are `cat` and `dog`.

   <br>

2. Import the `ImagePipeline` class and instantiate by providing the path of the parent path:

   ```python
   from pyimage.pipeline import ImagePipeline
   pipe = ImagePipeline('path/to/cat_dog')
   ```

   <br>

3. Read the images in by using the `read` function. The `read` function accepts an optional `sub_dirs` argument 
   which is a tuple of the sub-directory names. If no argument is provided, all the sub-directories are read.
   The images are stored as a list of list (of matrices) in the instance variable `img_lst2`. 
   
   ```python
   pipe.read(sub_dirs=('cat', 'dog'))
   ```
   
   <br>

4. Resize the images by providing the dimensions. The images are by default read in as a 3D tensor, therefore
   the dimension argument must be a tuple of 3.
   
   ```python
   pipe.resize((300, 300, 3))
   ```

   <br>

5. If you are interested to view some of your images anytime along your resizing/transformation steps, you can
   use the `show` function. The first argument is the name of sub-directory and the second argument is the nth
   image in the sub-directory you would want to view.
   
   ```python
   pipe.show('cat', 0)
   ```

   <br>

6. To transform all the images, use the `transform` function. The first arugment is the transformation function,
   usually a function from [skimage](http://scikit-image.org/). The second argument is a dictionary
   of the additional arguments needed for the transformation function. 

   ```python
   from skimage.color import rgb2gray
   pipe.transform(rgb2gray, {})
   pipe.show('cat', 0)
   ```

   <br>

   If you want to just transform one image instead of all the images to see what the effects are like, the third
   and four arguments are the name of the sub-directory and the nth image you want to apply the transformation to.
   The function will be applied to the one image, but not change the original copy.

   ```python
   from skimage.feature import canny
   pipe.transform(canny, {}, 'cat', 0)
   ```
   
   <br>

7. When you have done all the necessary transformations, call `vectorize`. The images will be flattened to form
   a feature matrix where each row are the pixels of an image. The class labels are also generated as a vector.
   The feature matrix and label vector are accessible in the instance variable `features` and `labels` respectively.
   
   ```python
   pipe.vectorize()
   pipe.features
   pipe.labels
   ```

<br>

References:

1. Jeremy Elson, John R. Douceur, Jon Howell, Jared Saul, Asirra: A CAPTCHA that Exploits Interest-Aligned Manual Image
   Categorization, in Proceedings of 14th ACM Conference on Computer and Communications Security (CCS), Association for
   Computing Machinery, Inc., Oct. 2007
