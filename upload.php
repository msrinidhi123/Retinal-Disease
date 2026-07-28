<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["image"])) {
    $targetDir = "upload/";
    if (!file_exists($targetDir)) {
        mkdir($targetDir, 0777, true);
    }

    $fileName   = uniqid() . "_" . basename($_FILES["image"]["name"]);
    $targetFile = $targetDir . $fileName;

    if (move_uploaded_file($_FILES["image"]["tmp_name"], $targetFile)) {
        // Run the Python script
        $command = escapeshellcmd("py -3.10 app.py " . escapeshellarg($targetFile));
        $output  = shell_exec($command);

        if (!$output) {
            echo json_encode(['error' => 'Prediction failed.']);
            exit();
        }

        // Trim and parse out the real confidence
        $output     = trim($output);
        $confidence = null;
        if (preg_match('/Confidence:\s*([\d\.]+)/', $output, $m)) {
            $confidence = (float)$m[1];
        }

        header('Content-Type: application/json');
        echo json_encode([
            'class'      => $output,
            'confidence' => $confidence   // now dynamic, not hard‑coded
        ]);
    } else {
        echo json_encode(['error' => 'Upload failed.']);
    }
} else {
    echo json_encode(['error' => 'Invalid request.']);
}
?>













