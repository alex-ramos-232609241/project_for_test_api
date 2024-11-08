from app.application import Application

def before_scenario(context, scenario):
    
    context.app = Application()
