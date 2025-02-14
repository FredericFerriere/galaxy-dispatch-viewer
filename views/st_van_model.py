from data import model as m
import views.st_model_page as mp

cur_model = m.Model.get_model('van')
mp.view_model(cur_model)