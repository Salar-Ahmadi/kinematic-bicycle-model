import numpy as np
import matplotlib.pyplot as plt


class Bicycle:
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

        self.L = 2
        self.lr = 1.2
        self.w_max = 1.22
        self.sample_time = 0.01

    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

    def step(self, v, w):
        w = np.clip(w, -self.w_max, self.w_max)

        self.delta += w * self.sample_time

        self.beta = np.arctan(self.lr * np.tan(self.delta) / self.L)

        self.xc += v * np.cos(self.theta + self.beta) * self.sample_time
        self.yc += v * np.sin(self.theta + self.beta) * self.sample_time
        self.theta += (
            v * np.cos(self.beta) * np.tan(self.delta) / self.L
        ) * self.sample_time


def plot_result(x_data, y_data, title):
    plt.figure()
    plt.axis("equal")
    plt.plot(x_data, y_data, label="Model")
    plt.title(title)
    plt.legend()
    plt.show()


def constant_steering_circle():
    sample_time = 0.01
    time_end = 20

    model = Bicycle()
    model.delta = np.arctan(2 / 10)

    t_data = np.arange(0, time_end, sample_time)
    x_data = np.zeros_like(t_data)
    y_data = np.zeros_like(t_data)

    for i in range(len(t_data)):
        x_data[i] = model.xc
        y_data[i] = model.yc
        model.step(np.pi, 0)

    plot_result(x_data, y_data, "Constant Steering Circle")


def steering_to_target_circle():
    sample_time = 0.01
    time_end = 20

    model = Bicycle()

    t_data = np.arange(0, time_end, sample_time)
    x_data = np.zeros_like(t_data)
    y_data = np.zeros_like(t_data)

    target_delta = np.arctan(2 / 10)

    for i in range(len(t_data)):
        x_data[i] = model.xc
        y_data[i] = model.yc

        if model.delta < target_delta:
            model.step(np.pi, model.w_max)
        else:
            model.step(np.pi, 0)

    plot_result(x_data, y_data, "Steering Toward Target Angle")


def square_path():
    sample_time = 0.01
    time_end = 60

    model = Bicycle()

    t_data = np.arange(0, time_end, sample_time)
    x_data = np.zeros_like(t_data)
    y_data = np.zeros_like(t_data)

    v_data = np.zeros_like(t_data)
    v_data[:] = 4

    w_data = np.zeros_like(t_data)

    w_data[670:670 + 100] = 0.753
    w_data[670 + 100:670 + 100 * 2] = -0.753

    w_data[2210:2210 + 100] = 0.753
    w_data[2210 + 100:2210 + 100 * 2] = -0.753

    w_data[3670:3670 + 100] = 0.753
    w_data[3670 + 100:3670 + 100 * 2] = -0.753

    w_data[5220:5220 + 100] = 0.753
    w_data[5220 + 100:5220 + 100 * 2] = -0.753

    for i in range(len(t_data)):
        x_data[i] = model.xc
        y_data[i] = model.yc
        model.step(v_data[i], w_data[i])

    plot_result(x_data, y_data, "Square Path")


def figure_eight_path():
    sample_time = 0.01
    time_end = 30

    model = Bicycle()

    t_data = np.arange(0, time_end, sample_time)
    x_data = np.zeros_like(t_data)
    y_data = np.zeros_like(t_data)

    v_data = np.zeros_like(t_data)
    w_data = np.zeros_like(t_data)

    delta_target = np.arctan(model.L / 8)

    v_data[:] = (2 * 2 * np.pi * 8) / 30

    cross1 = 375
    cross2 = 1900
    target_sign = 1

    for i in range(len(t_data)):
        x_data[i] = model.xc
        y_data[i] = model.yc

        if i == cross1 or i == cross2:
            target_sign *= -1

        delta_des = target_sign * delta_target

        if model.delta < delta_des - 1e-3:
            w = model.w_max
        elif model.delta > delta_des + 1e-3:
            w = -model.w_max
        else:
            w = 0

        w_data[i] = w
        model.step(v_data[i], w_data[i])

    plot_result(x_data, y_data, "Figure Eight Path")


if __name__ == "__main__":
    constant_steering_circle()
    steering_to_target_circle()
    square_path()
    figure_eight_path()