### Rainbow IQN CartPole Config ###

env = {
    "name": "cartpole",
    "action_type": "discrete",
    "render": False,
}

agent = {
    "name": "rainbow_iqn",
    "network": "rainbow_iqn",
    "gamma": 0.99,
    "explore_ratio": 0.2,
    "buffer_size": 50000,
    "batch_size": 32,
    "start_train_step": 2000,
    "target_update_period": 1000,
    # MultiStep
    "n_step": 3,
    # PER
    "alpha": 0.6,
    "beta": 0.4,
    "learn_period": 2,
    "uniform_sample_prob": 1e-3,
    # Noisy
    "noise_type": "factorized",  # [independent, factorized]
    # IQN
    "num_sample": 64,
    "embedding_dim": 64,
    "sample_min": 0.0,
    "sample_max": 1.0,
}

optim = {
    "name": "adam",
    "eps": 1e-2 / agent["batch_size"],
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
