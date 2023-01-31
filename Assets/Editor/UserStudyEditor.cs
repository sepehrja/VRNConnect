using UnityEditor;
using UnityEngine;

[CustomEditor(typeof(UserStudyScript))]
public class UserStudyEditor : Editor
{
    public override void OnInspectorGUI()
    {
        DrawDefaultInspector();
        
        UserStudyScript script = (UserStudyScript)target;

        if (GUILayout.Button("Reset Everything"))
        {
            script.RestFunction();
        }
        
        if (GUILayout.Button("Run User Study"))
        {
            script.RunUserStudy();
        }
        
        if (GUILayout.Button("WriteResults"))
        {
            script.WriteCSV(true);
        }
        
        if (GUILayout.Button("OnNext()"))
        {
            script.onNextClicked();
        }
        
        if (GUILayout.Button("OnFinish()"))
        {
            script.onFinishClicked();
        }
    }
}
