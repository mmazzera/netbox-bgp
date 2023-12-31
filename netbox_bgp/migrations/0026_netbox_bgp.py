# Generated by Django 4.0.6 on 2022-07-29 10:29

from django.db import migrations, models
import django.db.models.deletion


def use_core_asn(apps, schema_editor):
    """
    migrate bgpsession to core ASN.
    You must migrate all ASN objects for each ASN used in a BGPSession with the migration assistant
    available in v0.7.0 of this plugin before running this migration
    """
    BGPSession = apps.get_model('netbox_bgp', 'BGPSession')
    PluginASN = apps.get_model('netbox_bgp', 'ASN')
    CoreASN = apps.get_model('ipam', 'ASN')

    for bgpsession in BGPSession.objects.all():
        old_local_as = PluginASN.objects.get(id=bgpsession.local_as).number
        old_remote_as = PluginASN.objects.get(id=bgpsession.remote_as).number
        bgpsession.local_as = CoreASN.objects.get(asn=old_local_as).id
        bgpsession.remote_as = CoreASN.objects.get(asn=old_remote_as).id
        bgpsession.save()


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_bgp', '0025_netbox_bgp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asngroup',
            name='site',
        ),
        migrations.AlterField(
            model_name='bgpsession',
            name='local_as',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bgpsession',
            name='remote_as',
            field=models.BigIntegerField(),
        ),
        migrations.RunPython(
            code=use_core_asn,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name='bgpsession',
            name='local_as',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='local_as', to='ipam.asn'),
        ),
        migrations.AlterField(
            model_name='bgpsession',
            name='remote_as',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='remote_as', to='ipam.asn'),
        ),
        migrations.DeleteModel(
            name='ASN',
        ),
        migrations.DeleteModel(
            name='ASNGroup',
        ),
    ]
