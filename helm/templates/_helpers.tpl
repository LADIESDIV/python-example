{{/* vim: set filetype=mustache: */}}
{{/*
Check max override length.
*/}}
{{- define "python-example.checkNameOverrideLength" -}}
{{- if .Values.nameOverride -}}
{{- if gt (len .Values.nameOverride) 20 -}}
{{- fail "nameOverride cannot be longer than 20 characters" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Expand the name of the chart.
*/}}
{{- define "python-example.name" -}}
{{- include "python-example.checkNameOverrideLength" . -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "python-example.fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
