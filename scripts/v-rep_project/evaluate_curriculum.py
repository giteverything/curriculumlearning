import training_independent_joints as training
import os.path


## use the following to test the training script
# training.trainDQL(num_hidden_layers=2,
#                   num_neurons_per_hidden=50,
#                   num_episodes=10,
#                   max_steps_per_episode=2,
#                   e_min=0.01,
#                   model_saving_period=2,
#                   batch_size=2,
#                   replay_start_size=2,
#                   replay_memory_size=10,
#                   showGUI=True,
#                   velocity=0.3,
#                   model_to_load_file_path=None,
#                   use_variable_names=True,
#                   notes="testing algorithm")

#feed set of hyper params

# training.trainDQL(num_hidden_layers=2,
#                   num_neurons_per_hidden=50,
#                   num_episodes=3000,
#                   max_steps_per_episode=500,
#                   e_min=0.01,
#                   model_saving_period=100,
#                   batch_size=32,
#                   replay_start_size=50000,
#                   replay_memory_size=500000,
#                   showGUI=True,
#                   velocity=0.3,
#                   model_to_load_file_path=None,
#                   notes="back to positive rewards")

current_dir_path = os.path.dirname(os.path.realpath(__file__))
successful_model_1_ep3000 = os.path.join(
   current_dir_path,"trained_models_and_results",
   "model_and_results_2017-Jul-03_15-24-03-success","trained_model","final_model-3000")

model_ep400 = os.path.join(
   current_dir_path,"trained_models_and_results",
   "model_and_results_2017-Jul-03_15-24-03-success","saved_checkpoints","checkpoint_model-400")

model_2_ep3000 = os.path.join(
   current_dir_path,"trained_models_and_results",
   "model_and_results_2017-Jul-11_14-19-11","trained_model","final_model-3000")

training.trainDQL(num_hidden_layers=2,
                  num_neurons_per_hidden=50,
                  num_episodes=10,
                  max_steps_per_episode=500,
                  e_min=0.0,
                  model_saving_period=100,
                  batch_size=32,
                  replay_start_size=50000,
                  replay_memory_size=500000,
                  showGUI=True,
                  velocity=0.3,
                  model_to_load_file_path=model_2_ep3000,
                  use_variable_names=False,
                  notes="visualization")
