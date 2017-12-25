import se_feedback
import nx_feedback
import plots_to_pdf
import json_to_plots

feedback_obj= se_feedback.Feedback_client_Se('SolidEdge')
visual_obj = plots_to_pdf.VisualPDF(feedback_obj.se_dataframe, 'SolidEdge')
visual_obj.write_file(
    visual_obj.get_mainfile(
        visual_obj.draw_frame('SolidEdge'),
        visual_obj.draw_comments(feedback_obj.se_dataframe, 'SolidEdge'),
        feedback_obj.se_dataframe,
        'SolidEdge'),
    'SolidEdge')
visual_obj.visualize('SolidEdge')
print("Done SolidEdge")
feedback_obj= nx_feedback.Feedback_client_Nx('Nx')
visual_obj = plots_to_pdf.VisualPDF(feedback_obj.nx_dataframe, 'Nx')
visual_obj.write_file(
    visual_obj.get_mainfile(
        visual_obj.draw_frame('Nx'),
        visual_obj.draw_comments(feedback_obj.nx_dataframe, 'Nx'),
        feedback_obj.nx_dataframe,
        'Nx'),
    'Nx')
visual_obj.visualize('Nx')
print("Done NX")