### Rainbow DQN CartPole Config ###

env = {
    "name": "cartpole",
    "action_type": "discrete",
    "render": False,
}

agent = {
    "name": "rainbow",
    "network": "rainbow",
    "gamma": 0.99,
    "explore_ratio": 0.2,
    "buffer_size": 50000,
    "batch_size": 32,
    "start_train_step": 2000,
    "target_update_period": 500,
    # MultiStep
    "n_step": 3,
    # PER
    "alpha": 0.5,
    "beta": 0.4,
    "learn_period": 2,
    "uniform_sample_prob": 1e-3,
    # Noisy
    "noise_type": "factorized",  # [independent, factorized]
    # C51
    "v_min": -1,
    "v_max": 10,
    "num_support": 51,
}

optim = {
    "name": "adam",
    # "lr": 2.5e-4 / 4,
    "lr": 0.0001,
}

train = {
    "training": True,
    "load_path": None,
    "run_step": 100000,
    "print_period": 1000,
    "save_period": 10000,
    "eval_iteration": 10,
    # distributed setting
    "update_period": 8,
    "num_workers": 8,
}
