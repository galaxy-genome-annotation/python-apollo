from . import ApolloTestCase, wa


class MetricsTest(ApolloTestCase):

    def test_get_metrics(self):

        metrics = wa.metrics.get_metrics()

        assert 'version' in metrics
        assert 'gauges' in metrics
        assert 'counters' in metrics
        assert 'histograms' in metrics
        assert 'meters' in metrics
        assert 'timers' in metrics

        assert 'org.bbop.apollo.AnnotationEditorController.annotationEditorTimer' in metrics['timers']
