Adversarial Attacks on Object Detection Models Using Formal Verification Methods
======================
This project is the culmination of our Bachelor of Science in Computer Engineering at Bar-Ilan.

Installation and Setup
----------------------

Our project is tested on Python 3.7+ and PyTorch 1.11. It can be installed
easily into a conda environment. If you don't have conda, you can install
[miniconda](https://docs.conda.io/en/latest/miniconda.html).

```bash
# Remove the old environment, if necessary.
conda deactivate; conda env remove --name adversarial-attacks-od
# install all dependents into the adversarial-attacks-od environment
conda env create -f complete_verifier/environment.yml --name adversarial-attacks-od
# Activate the environment
conda activate adversarial-attacks-od
```

If you prefer to install packages manually rather than using a prepared conda
environment, you can refer to this [installation
script](/vnncomp_scripts/install_tool_general.sh).


Instructions
----------------------

In our project, you can find a unified front-end for the verifier, `abcrown.py`.  All parameters
for the verifier are defined in a `yaml` config file. For example, to run
robustness verification on a YOLOv5 network, you just run:

```bash
conda activate adversarial-attacks-od  # activate the conda environment
cd complete_verifier
python abcrown.py --config exp_configs/yolo.yaml
```

Data Set
----------------------
To run the project on any data set of your choice do as following:
1. choose images of the same size. and save them as a `.npy` file called `X_yolo.npy`
2. save the detections of the images before the attack and save them as a `.npy` file called `Y_yolo.npy`
3. place them both in this root direction `complete_verifier/datasets/yolo/`


Publications
----------------------


Developers and Copyright
----------------------
Our project was developed by a team from Bar-Ilan University University, Faculty of Engineering. Israel.


Main developers:  
* Omer Cohen, Bar-Ilan University
* Yael Leibovich Weiss, Bar-Ilan University

Advisors:  
* Avraham Raviv, Bar-Ilan University
* Hillel Kugler, Bar-Ilan University


This project utilizes the α,β-CROWN library for neural network verification developed by Verified Intelligence.

- α-CROWN: [Xu et al., 2021](https://arxiv.org/pdf/2011.13824.pdf)
- β-CROWN: [Wang et al., 2021](https://arxiv.org/pdf/2103.06624.pdf)

Here are the respective papers:

- Xu, K., Chen, H., Sharma, S., & others. (2021). Title of the α-CROWN paper. [Link](https://arxiv.org/pdf/2011.13824.pdf)
- Wang, L., Zhang, H., Sharma, S., & others. (2021). Title of the β-CROWN paper. [Link](https://arxiv.org/pdf/2103.06624.pdf)

For more information and to access the α,β-CROWN project, visit the repository: [https://github.com/Verified-Intelligence/alpha-beta-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN).


The project uses YOLOv5 as the neural network. For more information and to access the YOLOv5 project, visit the repository: [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5).


