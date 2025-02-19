from os.path import join, dirname, realpath

DISCIPLINE_MM_STR = 'Measurement and Monitoring'
DISCIPLINE_SS_STR = 'Social Sciences'
DISCIPLINE_ED_STR = 'Existing Data'
DISCIPLINE_CBM_STR = 'Code-Based Modeling'
DISCIPLINE_MAE_STR = 'Model Application and Evaluation'
DISCIPLINE_SAD_STR = 'Software and Application Development'
DISCIPLINE_ET_STR = 'Environmental Technology'

DISCIPLINE_CHOICES = (
  (DISCIPLINE_MM_STR, DISCIPLINE_MM_STR),
  (DISCIPLINE_SS_STR, DISCIPLINE_SS_STR)
  (DISCIPLINE_ED_STR, DISCIPLINE_ED_STR),
  (DISCIPLINE_CBM_STR, DISCIPLINE_CBM_STR),
  (DISCIPLINE_MAE_STR, DISCIPLINE_MAE_STR),
  (DISCIPLINE_SAD_STR, DISCIPLINE_SAD_STR),
  (DISCIPLINE_ET_STR, DISCIPLINE_ET_STR),
)

dir_path = dirname(realpath(__file__))
MODEL_LABELS_JSON_DIR = join(dir_path, './section_b_model_labels')
MODEL_LABELS_JSON_PATHS = {}
for choice, _ in DISCIPLINE_CHOICES:
  MODEL_LABELS_JSON_PATHS[choice] = join(
    MODEL_LABELS_JSON_DIR, choice.replace(' ', '-') + '.json')
